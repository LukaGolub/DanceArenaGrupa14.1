import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import NotFoundPage from './pages/notfoundpage.jsx'
import Login from './pages/login.jsx'
import Homepage from './pages/homepage.jsx'
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter([{
  path: "/homepage",
  element: <Homepage />,
  errorElement: <NotFoundPage />,
},
{
  path: "/login",
  element: <Login />,
}
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
