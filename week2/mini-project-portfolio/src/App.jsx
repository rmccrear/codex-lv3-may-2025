import './App.css'
import HeroImage from './components/HeroImage'

function App() {

  return (
    <>
      <HeroImage />
      {/* MAIN (Center website) */}
      <div className="main">

        <h1>MYLOGO.COM</h1>
        <hr />

        <h2>PORTFOLIO</h2>
        <p>Resize the browser window to see the responsive effect.</p>

        {/* Portfolio Gallery Grid */}
        <div className="row">
          <div className="column">
            <div className="content">
              <img src="/mountains.jpg" alt="Mountains" className="project-image" />
              <h3>My Work</h3>
              <p>Lorem ipsum..</p>
            </div>
          </div>
          <div className="column">
            <div className="content">
              <img src="/lights.jpg" alt="Lights" className="project-image" />
              <h3>My Work</h3>
              <p>Lorem ipsum..</p>
            </div>
          </div>
          <div className="column">
            <div className="content">
              <img src="/nature.jpg" alt="Nature" className="project-image" />
              <h3>My Work</h3>
              <p>Lorem ipsum..</p>
            </div>
          </div>
          <div className="column">
            <div className="content">
              <img src="/mountains.jpg" alt="Mountains" className="project-image" />
              <h3>My Work</h3>
              <p>Lorem ipsum..</p>
            </div>
          </div>
        </div>

        <div className="content">
          <img src="/bear.jpg" alt="Bear" className="project-image" />
          <h3>Some Other Work</h3>
          <p>Lorem ipsum..</p>
        </div>

        {/* END MAIN */}
      </div>
    </>
  )
}

export default App
