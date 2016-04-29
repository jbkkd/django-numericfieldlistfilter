function updateQueryStringParameter(url, key, value) {
  var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
  var separator = url.indexOf('?') !== -1 ? "&" : "?";
  if (url.match(re)) {
    return url.replace(re, '$1' + key + "=" + value + '$2');
  }
  else {
    return url + separator + key + "=" + value;
  }
}

(function($) {
    $(document).ready(function () {
        $('.numeric-field-filter-form').on('submit', function (e) {
            e.preventDefault();
            var $this = $(this);
            var field = $this.data('field').replace('-', '_');
            var $min_input = $this.children('.numeric-filter-min');
            var $max_input = $this.children('.numeric-filter-max');
            var min_value = $min_input.val();
            var max_value = $max_input.val();
            var location = window.location.pathname;
            if (min_value) {
                var min_value_qs_key = field + '__gte';
                location = updateQueryStringParameter(location, min_value_qs_key, min_value);
            }
            if (max_value) {
                var max_value_qs_key = field + '__lte';
                location = updateQueryStringParameter(location, max_value_qs_key, max_value);
            }
            window.location = location;
        });
    });
})(django.jQuery);