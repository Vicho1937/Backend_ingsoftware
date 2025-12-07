import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import '../styles/Auth.css'

function Register() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    password2: '',
    first_name: '',
    last_name: '',
    phone: ''
  })
  const [error, setError] = useState('')
  const [fieldErrors, setFieldErrors] = useState({})
  const [loading, setLoading] = useState(false)
  const { register } = useAuth()
  const navigate = useNavigate()

  const validateField = (name, value) => {
    let error = ''
    
    switch(name) {
      case 'first_name':
      case 'last_name':
        // Solo letras y espacios, entre 2 y 30 caracteres
        if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,30}$/.test(value)) {
          error = 'Solo letras, entre 2 y 30 caracteres'
        }
        break
      case 'username':
        // Alfanumérico, guiones bajos y guiones, 3-20 caracteres
        if (!/^[a-zA-Z0-9_-]{3,20}$/.test(value)) {
          error = 'Solo letras, números, _ y -, entre 3 y 20 caracteres'
        }
        break
      case 'email':
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
          error = 'Email inválido'
        }
        break
      case 'phone':
        // Opcional, pero si se ingresa debe ser válido
        if (value && !/^[\d\s()+\-]{8,15}$/.test(value)) {
          error = 'Formato de teléfono inválido'
        }
        break
      case 'password':
        if (value.length < 8) {
          error = 'Mínimo 8 caracteres'
        } else if (!/(?=.*[a-z])/.test(value)) {
          error = 'Debe contener al menos una minúscula'
        } else if (!/(?=.*[A-Z])/.test(value)) {
          error = 'Debe contener al menos una mayúscula'
        } else if (!/(?=.*\d)/.test(value)) {
          error = 'Debe contener al menos un número'
        }
        break
      case 'password2':
        if (value !== formData.password) {
          error = 'Las contraseñas no coinciden'
        }
        break
    }
    
    return error
  }

  const handleChange = (e) => {
    const { name, value } = e.target
    
    // Limitar caracteres especiales en nombres
    if (name === 'first_name' || name === 'last_name') {
      const sanitized = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]/g, '')
      setFormData({
        ...formData,
        [name]: sanitized
      })
      
      const error = validateField(name, sanitized)
      setFieldErrors({
        ...fieldErrors,
        [name]: error
      })
    } else {
      setFormData({
        ...formData,
        [name]: value
      })
      
      const error = validateField(name, value)
      setFieldErrors({
        ...fieldErrors,
        [name]: error
      })
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')

    // Validar todos los campos
    const errors = {}
    Object.keys(formData).forEach(key => {
      if (key !== 'phone') { // phone es opcional
        const error = validateField(key, formData[key])
        if (error) errors[key] = error
      }
    })

    if (Object.keys(errors).length > 0) {
      setFieldErrors(errors)
      setError('Por favor corrige los errores en el formulario')
      return
    }

    if (formData.password !== formData.password2) {
      setError('Las contraseñas no coinciden')
      return
    }

    setLoading(true)
    const result = await register(formData)
    
    if (result.success) {
      navigate('/')
    } else {
      setError(typeof result.error === 'string' ? result.error : JSON.stringify(result.error))
    }
    
    setLoading(false)
  }

  return (
    <div className="auth-page">
      <div className="auth-container">
        <h2>Crear Cuenta</h2>
        
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="form-row">
            <div className="form-group">
              <label>👤 Nombre:</label>
              <input
                type="text"
                name="first_name"
                value={formData.first_name}
                onChange={handleChange}
                required
                placeholder="Juan"
                maxLength="30"
                className={fieldErrors.first_name ? 'input-error' : ''}
              />
              {fieldErrors.first_name && (
                <span className="field-error">{fieldErrors.first_name}</span>
              )}
            </div>

            <div className="form-group">
              <label>👤 Apellido:</label>
              <input
                type="text"
                name="last_name"
                value={formData.last_name}
                onChange={handleChange}
                required
                placeholder="Pérez"
                maxLength="30"
                className={fieldErrors.last_name ? 'input-error' : ''}
              />
              {fieldErrors.last_name && (
                <span className="field-error">{fieldErrors.last_name}</span>
              )}
            </div>
          </div>

          <div className="form-group">
            <label>🔑 Usuario:</label>
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
              required
              placeholder="juanperez123"
              minLength="3"
              maxLength="20"
              className={fieldErrors.username ? 'input-error' : ''}
            />
            {fieldErrors.username && (
              <span className="field-error">{fieldErrors.username}</span>
            )}
            <small className="input-hint">Solo letras, números, guiones y guiones bajos</small>
          </div>

          <div className="form-group">
            <label>📧 Email:</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              placeholder="juan@ejemplo.com"
              className={fieldErrors.email ? 'input-error' : ''}
            />
            {fieldErrors.email && (
              <span className="field-error">{fieldErrors.email}</span>
            )}
          </div>

          <div className="form-group">
            <label>📱 Teléfono (opcional):</label>
            <input
              type="tel"
              name="phone"
              value={formData.phone}
              onChange={handleChange}
              placeholder="+56 9 1234 5678"
              className={fieldErrors.phone ? 'input-error' : ''}
            />
            {fieldErrors.phone && (
              <span className="field-error">{fieldErrors.phone}</span>
            )}
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>🔒 Contraseña:</label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                required
                minLength="8"
                placeholder="••••••••"
                className={fieldErrors.password ? 'input-error' : ''}
              />
              {fieldErrors.password && (
                <span className="field-error">{fieldErrors.password}</span>
              )}
              <small className="input-hint">Mín. 8 caracteres, 1 mayúscula, 1 minúscula, 1 número</small>
            </div>

            <div className="form-group">
              <label>🔒 Confirmar Contraseña:</label>
              <input
                type="password"
                name="password2"
                value={formData.password2}
                onChange={handleChange}
                required
                minLength="8"
                placeholder="••••••••"
                className={fieldErrors.password2 ? 'input-error' : ''}
              />
              {fieldErrors.password2 && (
                <span className="field-error">{fieldErrors.password2}</span>
              )}
            </div>
          </div>

          <button type="submit" disabled={loading} className="btn-primary">
            {loading ? '⏳ Registrando...' : '✨ Crear Cuenta'}
          </button>
        </form>

        <p className="auth-link">
          ¿Ya tienes cuenta? <Link to="/login">Inicia sesión aquí</Link>
        </p>
      </div>
    </div>
  )
}

export default Register
