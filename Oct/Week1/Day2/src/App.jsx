import './App.css'
import Home from './Home'
import About from './About'

function App() {
  let a=10;


 return(
  <div>
  Hello
  <div>welcome</div>
 <Home v={a}  str={"this is my string"} arr={[1,2,3]} obj={{name}}/>
  <About/>
  </div>
 ) 


}

export default App
