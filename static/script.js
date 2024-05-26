function loadError(){
    const url = new URL(window.location.href);
    const params = url.search.split("=");
    let param = '';
    if(params.length == 1){
        param = "";
    }else{
        param = params[1]+":Incorrect username/password ";
    }
    document.getElementById("error").innerHTML="<font color='red'>"+param+"</font>";
}

window.addEventListener("load",(event)=>{
    console.log(event);
    loadError();
})