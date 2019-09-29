$(function() {
  $("#selectable").selectable({
    selected: function() {
      var selectedItemList = $("#selected-item-list").empty();
      $(".ui-selected", this).each(function() {
        var index = $("#selectable img").index(this);
        selectedItemList.append((index + 1) + ", ");
      });
    }
  });
});