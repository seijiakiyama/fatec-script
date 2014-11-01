/**
 * Created by renzo on 10/8/14.
 */

$(document).ready(function () {
    var $appForm = $('#app-form');
    $appForm.hide();
    $('#mostrar-form-btn').click(function () {
        $appForm.slideToggle();
    });


    var $nomeInput = $('#nomeInput');
    var $linkInput = $('#linkInput');
    var $avaliacaoInput = $('#avaliacaoInput');
    var $descricaoInput = $('#descricaoInput');
    var $ajaxGif = $('#ajax-gif');

    var $nomeDiv = $('#nomeDiv');
    var $linkDiv = $('#linkDiv');
    var $avaliacaoDiv = $('#avaliacaoDiv');
    var $descricaoDiv = $('#descricaoDiv');

    $ajaxGif.hide();
    var $salvarBtn = $('#salvar-btn');
    var $helpNomeSpan = $('#help-nome');
    var $helpLinkSpan = $('#help-link');
    var $helpAvaliacaoSpan = $('#help-avaliacao');
    var $helpDescricaoSpan = $('#help-descricao');
    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha=function adicionarLinha(app) {
        var linha = '<tr id="tr' + app.id + '"> <td>' + app.nome + '</td>' +
            '<td>' + app.link + '</td>' +
            '<td>' + app.avaliacao + '</td>' +
            '<td>' + app.descricao + '</td>' +
            '<td><button id="bt' + app.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>' +
            '</td> </tr>';

        $corpoTabela.prepend(linha);

        var $linhaHtml = $('#tr' + app.id);

        $linhaHtml.hide();
        $linhaHtml.fadeIn();
        $('#bt' + app.id).click(function () {
            $linhaHtml.fadeOut();
            $.post('/appss/rest/delete',{'app_id':app.id}).success(function(){
                $linhaHtml.remove();
            }).error(function(){
                alert('Remoção não funcionou');
                $linhaHtml.fadeIn();
            });
        });
    }

    $.get('/appss/rest').success(function (listaDeapps) {
        for (var i = 0; i < listaDeapps.length; i += 1) {
            adicionarLinha(listaDeapps[i]);
        }

    });

    $salvarBtn.click(function () {
        var app = {nome: $nomeInput.val(),
            link: $linkInput.val(),
            avaliacao: $avaliacaoInput.val(),
            descricao: $descricaoInput.val()
        };

        $ajaxGif.slideDown();
        $salvarBtn.hide();
        var promessa = $.post('/appss/rest/save', app, 'json');
        promessa.success(function (app_do_servidor) {
            adicionarLinha(app_do_servidor);
            $nomeInput.val("");
            $linkInput.val("");
            $avaliacaoInput.val("");
            $descricaoInput.val("");
            $nomeDiv.removeClass('has-error');
            $linkDiv.removeClass('has-error');
            $avaliacaoDiv.removeClass('has-error');
            $descricaoDiv.removeClass('has-error');
            $helpNomeSpan.text('');
            $helpLinkSpan.text('');
            $helpAvaliacaoSpan.text('');
            $helpDescricaoSpan.text('');
        });


        promessa.error(function (erros) {
            if(erros.responseText != null) {
                erros.responseJSON = $.parseJSON(erros.responseText);
                if (erros.responseJSON != null && erros.responseJSON['errors'].nome != null) {
                    $nomeDiv.addClass('has-error');
                    $helpNomeSpan.text(erros.responseJSON['errors'].nome);
                }
                if (erros.responseJSON != null && erros.responseJSON['errors'].link != null) {
                    $linkDiv.addClass('has-error');
                    $helpLinkSpan.text(erros.responseJSON['errors'].link);
                }
                if (erros.responseJSON != null && erros.responseJSON['errors'].avaliacao != null) {
                    $avaliacaoDiv.addClass('has-error');
                    $helpAvaliacaoSpan.text(erros.responseJSON['errors'].avaliacao);
                }
                if (erros.responseJSON != null && erros.responseJSON['errors'].descricao != null) {
                    $descricaoDiv.addClass('has-error');
                    $helpDescricaoSpan.text(erros.responseJSON['errors'].descricao);
                }
            }
        });

        promessa.always(function () {
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
    });

});
