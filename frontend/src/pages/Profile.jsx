import { useState } from 'react'
import { useAuth } from '../context/AuthContext'
import api from '../services/api'
import '../styles/Profile.css'

function Profile() {
  const { user, updateUser } = useAuth()
  const [editing, setEditing] = useState(false)
  const [formData, setFormData] = useState({
    first_name: user?.first_name || '',
    last_name: user?.last_name || '',
    email: user?.email || '',
    phone: user?.phone || ''
  })
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    setMessage('')

    try {
      const response = await api.put('/auth/profile/', formData)
      updateUser(response.data)
      setMessage('Perfil actualizado exitosamente')
      setEditing(false)
    } catch (err) {
      setError('Error al actualizar el perfil')
    } finally {
      setLoading(false)
    }
  }

  const handleCancel = () => {
    setFormData({
      first_name: user?.first_name || '',
      last_name: user?.last_name || '',
      email: user?.email || '',
      phone: user?.phone || ''
    })
    setEditing(false)
    setError('')
  }

  return (
    <div className="profile-page">
      <div className="profile-container">
        <div className="profile-header">
          <div className="profile-avatar">
            👤
          </div>
          <h1>{user?.username}</h1>
          <p className="profile-role">{user?.role === 'admin' ? 'Administrador' : 'Usuario'}</p>
        </div>

        {message && <div className="success-message">{message}</div>}
        {error && <div className="error-message">{error}</div>}

        <div className="profile-info">
          {!editing ? (
            <>
              <div className="info-group">
                <label>Nombre:</label>
                <p>{user?.first_name} {user?.last_name}</p>
              </div>

              <div className="info-group">
                <label>Email:</label>
                <p>{user?.email}</p>
              </div>

              <div className="info-group">
                <label>Teléfono:</label>
                <p>{user?.phone || 'No especificado'}</p>
              </div>

              <div className="info-group">
                <label>Usuario desde:</label>
                <p>{new Date(user?.created_at).toLocaleDateString()}</p>
              </div>

              <button onClick={() => setEditing(true)} className="btn-primary">
                Editar Perfil
              </button>
            </>
          ) : (
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label>Nombre:</label>
                <input
                  type="text"
                  name="first_name"
                  value={formData.first_name}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Apellido:</label>
                <input
                  type="text"
                  name="last_name"
                  value={formData.last_name}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Email:</label>
                <input
                  type="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Teléfono:</label>
                <input
                  type="tel"
                  name="phone"
                  value={formData.phone}
                  onChange={handleChange}
                />
              </div>

              <div className="form-actions">
                <button type="submit" disabled={loading} className="btn-primary">
                  {loading ? 'Guardando...' : 'Guardar Cambios'}
                </button>
                <button type="button" onClick={handleCancel} className="btn-secondary">
                  Cancelar
                </button>
              </div>
            </form>
          )}
        </div>

        <div className="profile-stats">
          <h3>Estadísticas</h3>
          <div className="stats-grid">
            <div className="stat-card">
              <span className="stat-icon">⭐</span>
              <div>
                <p className="stat-value">0</p>
                <p className="stat-label">Reseñas</p>
              </div>
            </div>
            <div className="stat-card">
              <span className="stat-icon">❤️</span>
              <div>
                <p className="stat-value">0</p>
                <p className="stat-label">Favoritos</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Profile
