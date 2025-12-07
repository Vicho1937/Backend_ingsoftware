import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { MapPin, Navigation, Phone, Mail, Globe, Clock, FileText } from 'lucide-react'
import api from '../services/api'
import MapView from '../components/MapView'
import ReviewForm from '../components/ReviewForm'
import '../styles/RouteDetail.css'

function RouteDetail() {
  const { id } = useParams()
  const { user } = useAuth()
  const navigate = useNavigate()
  const [route, setRoute] = useState(null)
  const [loading, setLoading] = useState(true)
  const [showMap, setShowMap] = useState(false)

  useEffect(() => {
    loadRoute()
  }, [id])

  const loadRoute = async () => {
    try {
      const response = await api.get(`/routes/${id}/`)
      setRoute(response.data)
    } catch (error) {
      console.error('Error loading route:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleFavorite = async () => {
    if (!user) {
      alert('Debes iniciar sesión')
      navigate('/login')
      return
    }

    try {
      await api.post(`/routes/${id}/toggle_favorite/`)
      loadRoute()
    } catch (error) {
      console.error('Error toggling favorite:', error)
    }
  }

  const handleNavigate = () => {
    if (route.latitude && route.longitude) {
      const url = `https://www.google.com/maps/dir/?api=1&destination=${route.latitude},${route.longitude}`
      window.open(url, '_blank')
    }
  }

  const scrollToMap = () => {
    setShowMap(true)
    setTimeout(() => {
      document.getElementById('location-section')?.scrollIntoView({ behavior: 'smooth' })
    }, 100)
  }

  if (loading) {
    return <div className="loading">Cargando...</div>
  }

  if (!route) {
    return <div className="error">Ruta no encontrada</div>
  }

  return (
    <div className="route-detail">
      <div className="route-detail-header">
        {route.image_url && (
          <img src={route.image_url} alt={route.name} className="route-detail-image" />
        )}
        <div className="route-detail-title">
          <h1>{route.name}</h1>
          <div className="route-detail-meta">
            <span className="category-badge">{route.category_name}</span>
            <span className="rating-badge">
              ⭐ {route.average_rating?.toFixed(1) || '0.0'}
            </span>
            <span className="reviews-count">
              ({route.reviews_count} reseñas)
            </span>
          </div>
        </div>
        <button 
          className={`favorite-btn-large ${route.is_favorite ? 'active' : ''}`}
          onClick={handleFavorite}
        >
          {route.is_favorite ? '❤️ En Favoritos' : '🤍 Agregar a Favoritos'}
        </button>
      </div>

      <div className="route-detail-content">
        <section className="route-info">
          <div className="description-section">
            <div className="description-header">
              <h2>📄 Descripción</h2>
            </div>
            <div className="description-box">
              <p className="description-text">{route.description}</p>
            </div>
          </div>

          {route.opening_hours && (
            <div className="info-item">
              <Clock size={20} />
              <div>
                <strong>Horario de atención</strong>
                <p>{route.opening_hours}</p>
              </div>
            </div>
          )}

          <div className="location-section">
            <div className="location-box">
              <div className="location-header">
                <MapPin size={22} />
                <strong>Ubicación</strong>
              </div>
              <p className="location-address">{route.address}</p>
              <div className="location-actions">
                <button className="btn-location" onClick={scrollToMap}>
                  <MapPin size={18} />
                  Ver en mapa
                </button>
                <button className="btn-navigate" onClick={handleNavigate}>
                  <Navigation size={18} />
                  Cómo llegar
                </button>
              </div>
            </div>
          </div>
        </section>

        {route.latitude && route.longitude && (
          <section className="route-map" id="location-section">
            <div className="map-header">
              <h2>
                <MapPin size={28} />
                Ubicación en el mapa
              </h2>
              <p className="map-description">
                Visualiza la ubicación exacta del lugar y tu posición en tiempo real
              </p>
            </div>
            {showMap ? (
              <MapView 
                routes={[route]} 
                center={[parseFloat(route.latitude), parseFloat(route.longitude)]} 
                zoom={16}
                showUserLocation={true}
              />
            ) : (
              <div className="map-placeholder" onClick={() => setShowMap(true)}>
                <MapPin size={64} />
                <h3>Ver ubicación en el mapa</h3>
                <p>Haz clic para cargar el mapa interactivo</p>
                <button className="btn-primary">
                  <MapPin size={20} />
                  Cargar mapa
                </button>
              </div>
            )}
          </section>
        )}

        <section className="route-reviews">
          <h2>✏️ Reseñas</h2>
          
          {user ? (
            <ReviewForm routeId={id} onReviewSubmitted={loadRoute} />
          ) : (
            <div className="login-prompt">
              <div className="login-prompt-icon">🔒</div>
              <h3>Inicia sesión para dejar una reseña</h3>
              <p>Comparte tu experiencia con otros usuarios</p>
              <button 
                className="btn-primary"
                onClick={() => navigate('/login')}
              >
                Iniciar Sesión
              </button>
            </div>
          )}

          <div className="reviews-list">
            {route.reviews && route.reviews.length > 0 ? (
              route.reviews.map((review) => (
                <div key={review.id} className="review-item">
                  <div className="review-header">
                    <strong>{review.user.username}</strong>
                    <span className="review-rating">
                      {'⭐'.repeat(review.rating)}
                    </span>
                  </div>
                  <p className="review-comment">{review.comment}</p>
                  <small className="review-date">
                    {new Date(review.created_at).toLocaleDateString()}
                  </small>
                </div>
              ))
            ) : (
              <p className="no-reviews">Aún no hay reseñas. ¡Sé el primero en comentar!</p>
            )}
          </div>
        </section>
      </div>
    </div>
  )
}

export default RouteDetail
