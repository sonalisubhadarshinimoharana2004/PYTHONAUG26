import About from './About'
import './App.css'
import Home from './Home'

function App() {

  let a=10;

  return (
    <div>
      Hello

      <div>
        Welcome
      </div>

      <Home v={a}  str={"this is my string"} arr={[1,2,3]} obj={{name:'xyz',age:40}}/>
      <About/>
    </div>
  )
}

export default App

