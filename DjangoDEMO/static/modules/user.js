$(function(){
    console.log('user.js')
    $.get('/getUserByName',function(ret){
        console.log(ret)
    })
})