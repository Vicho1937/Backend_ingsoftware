import { useState } from 'react'
import api from '../services/api'
import '../styles/ReviewForm.css'

function ReviewForm({ routeId, onReviewSubmitted }) {
  const [rating, setRating] = useState(5)
  const [comment, setComment] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      await api.post(`/routes/${routeId}/add_review/`, {
        rating,
        comment
      })
      
      setRating(5)
      setComment('')
      if (onReviewSubmitted) {
        onReviewSubmitted()
      }
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al enviar la reseña')
    } finally {
      setLoading(false)
    }
  }

  return (
    <form className="review-form" onSubmit={handleSubmit}>
      <h3>Agregar Reseña</h3>
      
      {error && <div className="error-message">{error}</div>}
      
      <div className="form-group">
        <label>Calificación:</label>
        <div className="rating-input">
          {[1, 2, 3, 4, 5].map((star) => (
            <button
              key={star}
              type="button"
              className={`star-btn ${star <= rating ? 'active' : ''}`}
              onClick={() => setRating(star)}
            >
              ⭐
            </button>
          ))}
        </div>
      </div>

      <div className="form-group">
        <label>Comentario:</label>
        <textarea
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          required
          rows="4"
          placeholder="Comparte tu experiencia..."
        />
      </div>

      <button type="submit" disabled={loading} className="btn-submit">
        {loading ? 'Enviando...' : 'Enviar Reseña'}
      </button>
    </form>
  )
}

export default ReviewForm
