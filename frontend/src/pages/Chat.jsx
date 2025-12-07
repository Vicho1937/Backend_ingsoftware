import { useState, useRef, useEffect } from 'react'
import { useAuth } from '../context/AuthContext'
import { useNavigate } from 'react-router-dom'
import { MessageCircle, Lock } from 'lucide-react'
import api from '../services/api'
import '../styles/Chat.css'

function Chat() {
  const { user } = useAuth()
  const navigate = useNavigate()
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [sessionId] = useState(() => `session-${Date.now()}`)
  const [location, setLocation] = useState(null)
  const [locationPermission, setLocationPermission] = useState('prompt') // 'prompt', 'granted', 'denied'
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  // Solicitar ubicación al cargar el componente
  useEffect(() => {
    if (user && 'geolocation' in navigator) {
      // Verificar si ya tenemos permiso
      if (navigator.permissions) {
        navigator.permissions.query({ name: 'geolocation' }).then((result) => {
          setLocationPermission(result.state)
          if (result.state === 'granted') {
            getUserLocation()
          }
        })
      }
    }
  }, [user])

  const getUserLocation = () => {
    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const userLocation = {
            latitude: position.coords.latitude,
            longitude: position.coords.longitude
          }
          setLocation(userLocation)
          setLocationPermission('granted')
          console.log('Ubicación obtenida:', userLocation)
        },
        (error) => {
          console.error('Error obteniendo ubicación:', error)
          setLocationPermission('denied')
        }
      )
    }
  }

  const requestLocation = () => {
    getUserLocation()
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!input.trim()) return

    const userMessage = input.trim()
    setInput('')
    
    setMessages(prev => [...prev, { role: 'user', content: userMessage }])
    setLoading(true)

    try {
      const payload = {
        message: userMessage,
        session_id: sessionId
      }
      
      // Agregar ubicación si está disponible
      if (location) {
        payload.location = location
      }

      const response = await api.post('/chatbot/message/', payload)

      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: response.data.response 
      }])
    } catch (error) {
      console.error('Error sending message:', error)
      setMessages(prev => [...prev, { 
        role: 'error', 
        content: 'Lo siento, hubo un error al procesar tu mensaje.' 
      }])
    } finally {
      setLoading(false)
    }
  }

  const suggestedQuestions = [
    { emoji: '🗺️', text: '¿Qué lugares puedo visitar cerca de mí?' },
    { emoji: '🍽️', text: 'Recomiéndame restaurantes en Santiago' },
    { emoji: '🎭', text: 'Lugares de entretenimiento y cultura' },
    { emoji: '🌳', text: 'Parques y espacios al aire libre' },
    { emoji: '☕', text: 'Cafeterías para trabajar o estudiar' },
    { emoji: '🏛️', text: 'Lugares turísticos imperdibles' }
  ]

  const handleSuggestionClick = (questionText) => {
    setInput(questionText)
  }

  const clearChat = () => {
    setMessages([])
  }

  // Función para formatear el texto del bot (remover markdown)
  const formatBotMessage = (text) => {
    // Remover asteriscos de negrita (**texto** -> texto)
    let formatted = text.replace(/\*\*(.*?)\*\*/g, '$1')
    
    // Remover asteriscos simples (*texto* -> texto)
    formatted = formatted.replace(/\*(.*?)\*/g, '$1')
    
    // Mantener emojis y formato de lista con guiones
    return formatted
  }

  if (!user) {
    return (
      <div className="chat-page">
        <div className="chat-restricted">
          <div className="restricted-icon">
            <Lock size={64} />
          </div>
          <h2>Inicia sesión para usar el chat</h2>
          <p>El asistente virtual está disponible solo para usuarios registrados</p>
          <div className="restricted-features">
            <div className="feature-item">
              <MessageCircle size={24} />
              <span>Recomendaciones personalizadas</span>
            </div>
            <div className="feature-item">
              <MessageCircle size={24} />
              <span>Información detallada de lugares</span>
            </div>
            <div className="feature-item">
              <MessageCircle size={24} />
              <span>Ayuda en tiempo real</span>
            </div>
          </div>
          <button className="btn-primary" onClick={() => navigate('/login')}>
            Iniciar Sesión
          </button>
          <button className="btn-secondary" onClick={() => navigate('/register')}>
            Crear Cuenta
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="chat-page">
      <div className="chat-container">
        <div className="chat-header">
          <div className="chat-header-content">
            <div className="chat-avatar">
              <span className="avatar-icon">🤖</span>
              <span className="avatar-status"></span>
            </div>
            <div className="chat-header-info">
              <h2>Asistente Virtual</h2>
              <p className="status-text">
                <span className="status-dot"></span> Siempre disponible para ayudarte
                {location && <span className="location-badge">📍 Ubicación activa</span>}
              </p>
            </div>
          </div>
          {messages.length > 0 && (
            <button onClick={clearChat} className="clear-chat-btn" title="Limpiar conversación">
              🗑️
            </button>
          )}
        </div>

        {/* Banner de solicitud de ubicación */}
        {locationPermission !== 'granted' && (
          <div className="location-banner">
            <div className="location-banner-content">
              <span className="location-icon">📍</span>
              <div className="location-text">
                <strong>Activa tu ubicación</strong>
                <p>Obtén recomendaciones más precisas de lugares cercanos a ti</p>
              </div>
              {locationPermission === 'denied' ? (
                <p className="location-denied">
                  Ubicación denegada. Actívala en la configuración de tu navegador.
                </p>
              ) : (
                <button onClick={requestLocation} className="location-btn">
                  Activar Ubicación
                </button>
              )}
            </div>
          </div>
        )}

        <div className="chat-messages">
          {messages.length === 0 ? (
            <div className="chat-welcome">
              <div className="welcome-icon">👋</div>
              <h3>¡Hola{user ? `, ${user.first_name || user.username}` : ''}!</h3>
              <p className="welcome-subtitle">Soy tu asistente virtual de Ruta Local</p>
              
              <div className="chat-capabilities">
                <div className="capability-item">
                  <span className="capability-icon">🗺️</span>
                  <span>Información sobre lugares y rutas</span>
                </div>
                <div className="capability-item">
                  <span className="capability-icon">⭐</span>
                  <span>Recomendaciones personalizadas</span>
                </div>
                <div className="capability-item">
                  <span className="capability-icon">🔍</span>
                  <span>Buscar lugares específicos</span>
                </div>
                <div className="capability-item">
                  <span className="capability-icon">❓</span>
                  <span>Ayuda sobre la plataforma</span>
                </div>
              </div>
              
              <p className="chat-suggestion-title">💬 Preguntas sugeridas</p>
              <div className="chat-suggestions">
                {suggestedQuestions.map((question, index) => (
                  <button
                    key={index}
                    className="suggestion-btn"
                    onClick={() => handleSuggestionClick(question.text)}
                  >
                    <span className="suggestion-emoji">{question.emoji}</span>
                    <span className="suggestion-text">{question.text}</span>
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <>
              {messages.map((message, index) => (
                <div key={index} className={`message message-${message.role}`}>
                  <div className="message-avatar">
                    {message.role === 'user' ? (
                      <span className="user-avatar">{user?.first_name?.[0] || user?.username?.[0] || '👤'}</span>
                    ) : message.role === 'assistant' ? (
                      <span className="bot-avatar">🤖</span>
                    ) : (
                      <span className="error-avatar">⚠️</span>
                    )}
                  </div>
                  <div className="message-bubble">
                    <div className="message-content" style={{ whiteSpace: 'pre-wrap' }}>
                      {message.role === 'assistant' ? formatBotMessage(message.content) : message.content}
                    </div>
                  </div>
                </div>
              ))}
              {loading && (
                <div className="message message-assistant">
                  <div className="message-avatar">
                    <span className="bot-avatar">🤖</span>
                  </div>
                  <div className="message-bubble">
                    <div className="typing-indicator">
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                  </div>
                </div>
              )}
            </>
          )}
          <div ref={messagesEndRef} />
        </div>

        <form onSubmit={handleSubmit} className="chat-input-form">
          <div className="input-wrapper">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Escribe tu mensaje..."
              disabled={loading}
              className="chat-input"
              autoFocus
            />
            <button 
              type="submit" 
              disabled={loading || !input.trim()} 
              className="chat-send-btn"
              title="Enviar mensaje"
            >
              {loading ? (
                <span className="loading-spinner">⏳</span>
              ) : (
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M22 2L11 13" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <path d="M22 2L15 22L11 13L2 9L22 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Chat
