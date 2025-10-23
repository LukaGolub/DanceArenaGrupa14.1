import '../styles/homepage.css';
import Navbar from '../components/navbar.jsx';

function homepage({ setPage }) {
    return (
        <div className="homepage-container">
            <Navbar
                setPage={setPage} />
            <div className="homepage-content-container">
                <p>Uspješno ulogirani!</p>
                <p>Dobrodošao Taj i taj (taj.taj@gmail.com)!</p>
                <img src="/gifs/the greatest dancer of all.gif" alt="Description of your GIF" />
            </div>
        </div>
    )
};

export default homepage;