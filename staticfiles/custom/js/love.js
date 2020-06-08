function love(array) {
    var hold = [],
            result,
            newArray;
    if (array.length > 2) {
            newArray = array.map(function(item, index, array) {
                    return item + array[index + 1];
            });
            newArray.forEach(function(item) {
                    if (typeof item === "number" && !isNaN(item)) {
                            if (item < 10) {
                                    hold.push(item);
                            } else if (item > 9) {
                                    console.log('Splitting' + item + " into " + item.toString()[0] + " and " + item.toString()[1]);
                                    hold.push(parseInt(item.toString()[0]));
                                    hold.push(parseInt(item.toString()[1]));
                            }
                    } else {
                            console.log("failed number check: " + item);
                    }
            });
            love(hold);
    } else {
            document.getElementById('result').textContent = array[0] + "" + array[1] + "%";
            result = array[0] + "" + array[1] + "%";
            return result;
    }
}


var lovers = setInterval(function() {
var r_num = Math.floor(Math.random() * 5) + 1;
var r_size = Math.floor(Math.random() * 20) + 10;
var r_left = Math.floor(Math.random() * 100) + 1;
var r_bg = Math.floor(Math.random() * 25) + 100;
var r_time = Math.floor(Math.random() * 5) + 5;

$('.bg_heart').append("<div class='heart' style='width:" + r_size + "px;height:" + r_size + "px;left:" + r_left + "%;background:rgba(255," + (r_bg - 25) + "," + r_bg + ",1);-webkit-animation:lovers " + r_time + "s ease;-moz-animation:lovers " + r_time + "s ease;-ms-animation:lovers " + r_time + "s ease;animation:lovers " + r_time + "s ease'></div>");

$('.bg_heart').append("<div class='heart' style='width:" + (r_size - 10) + "px;height:" + (r_size - 10) + "px;left:" + (r_left + r_num) + "%;background:rgba(255," + (r_bg - 25) + "," + (r_bg + 25) + ",1);-webkit-animation:lovers " + (r_time + 5) + "s ease;-moz-animation:lovers " + (r_time + 5) + "s ease;-ms-animation:lovers " + (r_time + 5) + "s ease;animation:lovers " + (r_time + 5) + "s ease'></div>");

$('.heart').each(function() {
    var top = $(this).css("top").replace(/[^-\d\.]/g, '');
    var width = $(this).css("width").replace(/[^-\d\.]/g, '');
    if (top <= -100 || width >= 150) {
        $(this).detach();
    }
});
}, 5000);