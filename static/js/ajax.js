$.ajax({
    type: 'GET',
    url: "http://127.0.0.1:5000/pie_nest_data",
    dataType: 'json',
    success: function (data) {
        console.log(data);
        //html原本的js代码
    }
});