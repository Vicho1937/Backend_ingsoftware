import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './styles/index.css'
import { AuthProvider } from './context/AuthContext.jsx'

console.log('Main.jsx loaded')
console.log('Root element:', document.getElementById('root'))

try {
  ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
      <AuthProvider>
        <App />
      </AuthProvider>
    </React.StrictMode>,
  )
  console.log('React app rendered')
} catch (error) {
  console.error('Error rendering app:', error)
  document.body.innerHTML = `<div style="color: white; padding: 20px; font-family: monospace;">
    <h1>Error al cargar la aplicación</h1>
    <pre>${error.message}</pre>
    <pre>${error.stack}</pre>
  </div>`
}
