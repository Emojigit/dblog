$(document).ready(function(){
    $replyto_select = $("#replyto");
    $form_reply_goto = $("#form-reply-goto");
    $(".replyClick").click(function(e){
        $this = $(this);
        replyto = $this.attr("replyto");
        $replyto_select.val(replyto).change();
    });
    const check_form_reply_goto = (function(){
        if ($replyto_select.val() == "0") {
            $form_reply_goto.hide();
            return false;
        }
        $form_reply_goto.show();
        return true;
    });
    $("#form-reply-goto").click(function(e){
        e.preventDefault();
        if (check_form_reply_goto()) {
            location.hash = "comment-".concat($replyto_select.val());
        }
    });
    $replyto_select.change(check_form_reply_goto);
});
