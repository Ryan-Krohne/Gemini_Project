import { faDev, faGithub, faInstagram, faLinkedin } from "@fortawesome/free-brands-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const Footer = () => {
    return (
        <div className="footer">
            <div className="footer-container">
                <div className="footer-section about-section">
                    <h2 className="section-heading">About Us</h2>
                    <p className="section-content"> This is PixelInfo Inc., a project by Anthony and Ryan. 
                    The purpose of this application is to create infographics for marketing teams. Whether
                     its to speed up the brainstorming process infographic organization or written content
                     creation. We intend to fulfill this endevour.</p>

                     <div className="footer-section">
                        <h2 className="section-heading">Technology Used</h2>
                        <ul className="service-list" style={{ marginLeft: '5%' }}>
                            <li>Frontend: Vite React</li>
                            <li>Backend: Python Flask</li>
                            <li>Google's Gemini</li>
                            <li>Templates: Canva</li>
                        </ul>
                    </div>
                </div>
                <div className="footer-section contact-section">
                    <h2 className="section-heading">Contact Us</h2>
                    <p className="section-content">Feel free to reach out to us at:</p>
                    <div className="social-section">
                        <div><h3 className="social-heading">Anthony Social Media</h3></div>
                        <div className="icons-section">
                            <a target="_blank" rel="noreferrer" href="https://github.com/Gavisito"> <FontAwesomeIcon className="icons" icon={faGithub} color="white"/></a>
                            <a target="_blank" rel="noreferrer" href="https://www.linkedin.com/in/agavivasq/"> <FontAwesomeIcon className="icons" icon={faLinkedin} color="white"/></a>
                        </div>
                    </div>
                    <div className="social-section">
                        <div><h3 className="social-heading">Ryan Social Media</h3></div>
                        <div className="icons-section">
                            <a target="_blank" rel="noreferrer" href="https://github.com/Ryan-Krohne"> <FontAwesomeIcon className="icons" icon={faGithub} color="white"/></a>
                            <a target="_blank" rel="noreferrer" href="https://www.linkedin.com/in/ryankrohne"> <FontAwesomeIcon className="icons" icon={faLinkedin} color="white"/></a>
                        </div>
                    </div>
                </div>
            </div>
            <div className="footer-bottom">
                <p className="copyright">© {new Date().getFullYear()} PixelInfo Inc. All rights reserved.</p>
            </div>
        </div>
    );
};

export default Footer;






