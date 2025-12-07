import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { Trash2, CheckSquare, Square, Heart, Sparkles, MapPin } from 'lucide-react'
import api from '../services/api'
import RouteCard from '../components/RouteCard'
import '../styles/Favorites.css'

function Favorites() {
  const [favorites, setFavorites] = useState([])
  const [loading, setLoading] = useState(true)
  const [selectedIds, setSelectedIds] = useState([])
  const [deleting, setDeleting] = useState(false)

  useEffect(() => {
    loadFavorites()
  }, [])

  const loadFavorites = async () => {
    try {
      const response = await api.get('/favorites/')
      const favoritesData = response.data.results || response.data
      setFavorites(favoritesData.map(fav => fav.route))
    } catch (error) {
      console.error('Error loading favorites:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleFavoriteToggle = () => {
    loadFavorites()
    setSelectedIds([])
  }

  const toggleSelection = (id) => {
    setSelectedIds(prev => 
      prev.includes(id) 
        ? prev.filter(selectedId => selectedId !== id)
        : [...prev, id]
    )
  }

  const toggleSelectAll = () => {
    if (selectedIds.length === favorites.length) {
      setSelectedIds([])
    } else {
      setSelectedIds(favorites.map(fav => fav.id))
    }
  }

  const handleDeleteSelected = async () => {
    if (selectedIds.length === 0) return

    const confirmMessage = selectedIds.length === 1
      ? '¿Estás seguro de que quieres eliminar este favorito?'
      : `¿Estás seguro de que quieres eliminar ${selectedIds.length} favoritos?`

    if (!window.confirm(confirmMessage)) return

    setDeleting(true)
    try {
      await Promise.all(
        selectedIds.map(id => api.post(`/routes/${id}/toggle_favorite/`))
      )
      await loadFavorites()
      setSelectedIds([])
    } catch (error) {
      console.error('Error deleting favorites:', error)
      alert('Error al eliminar favoritos. Intenta de nuevo.')
    } finally {
      setDeleting(false)
    }
  }

  if (loading) {
    return <div className="loading">Cargando favoritos...</div>
  }

  return (
    <div className="favorites-page">
      <div className="favorites-header">
        <div className="header-title">
          <Heart size={36} className="heart-icon" />
          <div>
            <h1>Mis Favoritos</h1>
            <p>Lugares que has guardado para visitar más tarde</p>
          </div>
        </div>
        
        {favorites.length > 0 && (
          <div className="favorites-actions">
            <button 
              className="btn-select-all"
              onClick={toggleSelectAll}
            >
              {selectedIds.length === favorites.length ? (
                <>
                  <CheckSquare size={20} />
                  Deseleccionar Todo
                </>
              ) : (
                <>
                  <Square size={20} />
                  Seleccionar Todo
                </>
              )}
            </button>
            
            {selectedIds.length > 0 && (
              <button 
                className="btn-delete"
                onClick={handleDeleteSelected}
                disabled={deleting}
              >
                <Trash2 size={20} />
                {deleting 
                  ? 'Eliminando...' 
                  : `Eliminar (${selectedIds.length})`
                }
              </button>
            )}
          </div>
        )}
      </div>

      {favorites.length === 0 ? (
        <div className="no-favorites">
          <div className="no-favorites-animation">
            <div className="empty-heart">
              <Heart size={80} />
            </div>
            <Sparkles className="sparkle sparkle-1" size={24} />
            <Sparkles className="sparkle sparkle-2" size={20} />
            <Sparkles className="sparkle sparkle-3" size={18} />
          </div>
          <h2>Tu lista de favoritos está vacía</h2>
          <p>Descubre lugares increíbles y guárdalos para visitarlos después</p>
          <div className="empty-features">
            <div className="empty-feature">
              <MapPin size={24} />
              <span>Explora lugares cercanos</span>
            </div>
            <div className="empty-feature">
              <Heart size={24} />
              <span>Guarda tus favoritos</span>
            </div>
            <div className="empty-feature">
              <Sparkles size={24} />
              <span>Organiza tu itinerario</span>
            </div>
          </div>
          <Link to="/routes" className="btn-primary btn-explore">
            <MapPin size={20} />
            Explorar Lugares
          </Link>
        </div>
      ) : (
        <div className="favorites-content">
          <div className="favorites-stats">
            <span className="stat-badge">
              {favorites.length} {favorites.length === 1 ? 'Lugar Guardado' : 'Lugares Guardados'}
            </span>
            {selectedIds.length > 0 && (
              <span className="selection-badge">
                {selectedIds.length} seleccionado{selectedIds.length > 1 ? 's' : ''}
              </span>
            )}
          </div>

          <div className="routes-grid">
            {favorites.map((route) => (
              <div 
                key={route.id} 
                className={`favorite-item ${selectedIds.includes(route.id) ? 'selected' : ''}`}
              >
                <div 
                  className="selection-checkbox"
                  onClick={() => toggleSelection(route.id)}
                >
                  {selectedIds.includes(route.id) ? (
                    <CheckSquare size={24} className="checkbox-icon checked" />
                  ) : (
                    <Square size={24} className="checkbox-icon" />
                  )}
                </div>
                <RouteCard 
                  route={{ ...route, is_favorite: true }}
                  onFavoriteToggle={handleFavoriteToggle}
                  showRemoveButton={true}
                />
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

export default Favorites
