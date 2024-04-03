import React, { useState } from 'react';
import { Nav, Navbar, NavItem } from 'react-bootstrap';
import { Link, NavLink } from 'react-router-dom';

const Navigation = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen((prevState) => !prevState);
  };

  const handleNavLinkClick = () => {
    // Close the menu on mobile after clicking a link
    setMenuOpen(false);
  };

  return (
    <Navbar className="navigation" fixed="top" expand="sm">
      <>
        <div className="branding">
          <div>
            <a href="#home" className="company-logo">
              <img src="/vite.svg" className={`gavipic ${isMenuOpen ? 'active' : ''}`} alt="Logo" />
            </a>
          </div>
          <div>
            <a href="/" className={`company-name ${isMenuOpen ? 'active' : ''}`}>PixelInfo.Inc</a>
          </div>
        </div>
        <Nav className={`nav ${isMenuOpen ? 'active' : ''}`}>
            <NavItem>
                <Link to="/" className="nav-link">Home</Link>
            </NavItem>
            <NavItem>
                <Link to="/geminipage" className="nav-link">Generator</Link>
            </NavItem>
            <NavItem>
                <Link to="/contact" className="nav-link">Contact</Link>
            </NavItem>
        </Nav>
        <div className={`ham-icon ${isMenuOpen ? 'active' : ''}`} onClick={toggleMenu}>
          <span className="bar"></span>
          <span className="bar"></span>
          <span className="bar"></span>
        </div>
      </>
    </Navbar>
  );
};

export default Navigation;
