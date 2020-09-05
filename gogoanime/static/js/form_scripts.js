$(document).ready(function() {
    $('#VideoURLForm').one('submit', function() {
      $(this).find('input[type="submit"]').attr('disabled','disabled');
      $("<div />").addClass("overlay").append($("<div />").addClass("loader")).insertAfter(".wrapper");
    });
    $("label").remove();
    $("input[name='video_url']").prop("placeholder", "Enter a URL like https://www2.gogoanime.video/naruto-episode-1");
    $("select[name='site'] option[value='']").text("Choose a site");
    $("select[name='host'] option[value='']").text("Choose a host");
});