import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { Heart, X } from 'lucide-react'
import api from '../services/api'
import '../styles/RouteCard.css'

function RouteCard({ route, onFavoriteToggle, showRemoveButton = false }) {
  const { user } = useAuth()
  const navigate = useNavigate()

  const handleFavorite = async (e) => {
    e.preventDefault()
    e.stopPropagation()
    
    if (!user) {
      if (window.confirm('Debes iniciar sesión para agregar favoritos. ¿Ir a iniciar sesión?')) {
        navigate('/login')
      }
      return
    }

    // Si está en la página de favoritos y es favorito, pedir confirmación
    if (showRemoveButton && route.is_favorite) {
      if (!window.confirm('¿Estás seguro de que quieres eliminar este favorito?')) {
        return
      }
    }

    try {
      await api.post(`/routes/${route.id}/toggle_favorite/`)
      if (onFavoriteToggle) {
        onFavoriteToggle(route.id)
      }
    } catch (error) {
      console.error('Error toggling favorite:', error)
    }
  }

  return (
    <Link to={`/routes/${route.id}`} className="route-card">
      <div className="route-card-image">
        {route.image_url ? (
          <img src={route.image_url} alt={route.name} />
        ) : (
          <div className="route-card-placeholder">
            <span className="route-category-icon">{route.category_icon || '📍'}</span>
          </div>
        )}
        <button 
          className={`favorite-btn ${route.is_favorite ? 'active' : ''} ${!user ? 'locked' : ''} ${showRemoveButton && route.is_favorite ? 'remove-mode' : ''}`}
          onClick={handleFavorite}
          title={!user ? 'Inicia sesión para agregar a favoritos' : showRemoveButton && route.is_favorite ? 'Eliminar de favoritos' : route.is_favorite ? 'Quitar de favoritos' : 'Agregar a favoritos'}
        >
          {showRemoveButton && route.is_favorite ? (
            <X size={20} strokeWidth={3} />
          ) : (
            <Heart size={20} fill={route.is_favorite ? 'currentColor' : 'none'} />
          )}
        </button>
      </div>
      
      <div className="route-card-content">
        <h3>{route.name}</h3>
        <p className="route-category">{route.category_name}</p>
        <p className="route-description">{route.description}</p>
        <div className="route-card-footer">
          <div className="route-rating">
            ⭐ {route.average_rating?.toFixed(1) || '0.0'}
          </div>
          <div className="route-reviews">
            💬 {route.reviews_count || 0} reseñas
          </div>
        </div>
        <p className="route-address">📍 {route.address}</p>
      </div>
    </Link>
  )
}

export default RouteCard
