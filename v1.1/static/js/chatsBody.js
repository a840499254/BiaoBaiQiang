var userid = "u" + parseInt((new Date()).valueOf());
function refreshList() {
    var items = getList();
    // console.log(items);
    for(var i in items) {
        // console.log(i);
        var text = "[" + items[i][0] + "] " + items[i][1];
        document.getElementsByClassName("message-box")[0].innerHTML += "<p class='chat-item'>" + text + "</p>";
    }
}
function submitText() {
    var state = submit(userid);
    if(state){
        refreshList();
    }
}
refreshList();