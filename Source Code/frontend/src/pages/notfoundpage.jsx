import { Link } from "react-router-dom";

function NotFoundPage() {
    return (
        <div>ERROR 404 Page not found
            <Link to="/"> Go to homepage</Link>
        </div>
    )
}
export default NotFoundPage;