function getList() {
    document.getElementsByClassName("message-box")[0].innerHTML = "";
    var itresult = {};
    $.ajax({
        url: "/chatList",
        data: {},
        type: "POST",
        dataType: "json",
        async: false,
        success: function (result) {
            var keys = Object.keys(result)
            keys.reverse();
            var items = [];
            for(var k in keys) {
                items.push(result[keys[k]]);
                // console.log(keys[k]);
            }
            console.log(items);
            itresult = items;
        }
    });
    console.log(itresult);
    return itresult;
}
