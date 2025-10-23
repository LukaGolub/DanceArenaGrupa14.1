import '../styles/navbar.css';

function Navbar({ setPage }) {
    return (
        <div className="navbar">
            <div className="logo-text-container" onClick={() => setPage('login')}>
                <img src="/pictures/logo.png" alt="Dance Arena Logo" className="navbar-logo" />
                <img src="/pictures/tekst.png" alt="Dance Arena Title" className="navbar-text" />
            </div>
            <div className="nav-links">
                <p className="nav-link">Home</p>
                <p className="nav-link">About</p>
                <p className="nav-link">Contact</p>
            </div>
            <div className="account-section">
                <img src="/pictures/user icon.png" alt="User Icon" className="user-icon" />
            </div>

        </div>
    )
};

export default Navbar;