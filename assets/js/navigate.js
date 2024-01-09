
$(document).ready(function() {
    
    $("#nav_1").click(function() {
        var root_path = get_root_path();
        location.href = root_path;
    });

    $("#nav_2").click(function() {
        var root_path = get_root_path();
        location.href = root_path + "/publications";
    })
})

function get_root_path() {
    var full_path = window.document.location.href;
    var words = full_path.split('/');
    var root_path = words[0] + '//' + words[2];
    return root_path;
}