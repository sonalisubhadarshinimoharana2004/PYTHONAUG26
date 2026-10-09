function Home(props){
    return(
        <div>this is home page
        < br />
        value : {props.v}
        < br />
        string : {props.str}
        < br />
        Array value : {props.arr}
        < br />
        Object value : {JSON.stringify(props.obj)}
        < br />
        Object name : {props.obj.name}

    </div>
    )
    
   

}
export default Home