const realfilebutton = document.getElementById("file")
const customebutton = document.getElementById("button_file")
const text = document.getElementById("value")

customebutton.addEventListener('click' , ()=>{
    realfilebutton.click();
});

realfilebutton.addEventListener('change', ()=>{
    if(realfilebutton.value){
        text.innerText = realfilebutton.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
    }
    else{
        text.innerText = "No File input";
    }
})