/* Puts the included jQuery into our own namespace using noConflict and passing
 * it 'true'. This ensures that the included jQuery doesn't pollute the global
 * namespace (i.e. this preserves pre-existing values for both window.$ and
 * window.jQuery).
 */
var django = {
    "jQuery": jQuery.noConflict(true)
};

(function($) {
    $(document).ready(function() {
        $(".required").each(function (i, elem) {
            var inp = $(elem).next("input,textarea");
            inp.attr("required", "required");
            inp.attr("placeholder", "Required");
        });
        $("#searchbar").each(function(i, elem) {elem.type = "search";});
    });
})(django.jQuery);