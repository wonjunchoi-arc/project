import React, {useState} from 'react'

const Counter = () => {
    const [ number, setnumber] = useState(0)

    return(
        <><h2>{number}</h2>
        <h4>{item}</h4> 
        <button onClick = {()=>setnumber(number+1)}>+</button>
        <button onClick= {()=>setnumber(number-1)}>-</button>
        </>
    )
}
export default Counter