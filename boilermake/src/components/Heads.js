import React from "react";
import './heads.css';

function Heads(props){
    return <div className="note">
        <h1>{props.name}</h1>
        <p >{props.text} </p>
        <p><a className="btn btn-secondary" href={props.link} role="button">View details &raquo;</a></p>
      </div>;
}

export default Heads;
