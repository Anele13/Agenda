$(document).ready(function() {
  crearBarraEventos();
  crearCalendario();
})

function crearCalendario() {
  // Calendario
  $('#calendarioWeb').fullCalendar({
    header:{
      left: 'today,prev,next',
      center: 'title',
      right:'agendaWeek,btnExportar'
    },
    editable:true,
    droppable: true,
    customButtons: generarBotones(),
    resources: getEventos(),
    dayClick:function() {
       clickDia();
    },
    eventOverlap:function(stillEvent, movingEvent) {
      if (stillEvent.persona == movingEvent.persona) {
        return true;
      }
      else{
        return false;
      }
    }
  });
}

function crearBarraEventos() {
  // Barra lateral de eventos draggables
  $('#external-events .fc-event').each(function() {
    $(this).data('event', {
      title: $.trim($(this).text()), // use the element's text as the event title
      stick: true, // maintain when user navigates (see docs on the renderEvent method)
      editable: true,
      color: $(this).data('color')
    });
    // make the event draggable using jQuery UI
    $(this).draggable({
      zIndex: 999,
      revert: true,      // will cause the event to go back to its
      revertDuration: 0,  //  original position after the drag
    });
  });
}

//Genera los botones custom que quieras poner
function generarBotones() {
  customButtons = {
    btnExportar:{
      text: 'Click',
      click: function() {
        alert("click");
      }
    }
  }
  return customButtons
}


//eventos
//recibe 2 eventos, el que se mueve y el que esta. esto determina si se pueden solapar

//es el evento que se ejecuta cuando haces click en un dia
function clickDia(date, jsEvent, view) {
  $(this).css('background-color','red');
  $('#exampleModal').modal();
}

function dropDesdeBarra(date, jsEvent, ui, resourceId) {
  date.className = "team1";
}

function checkOverlap(stillEvent, movingEvent) {
  console.log(stillEvent.materia);
  if (stillEvent.materia == 1 ) {
    return true;
  }
  else{
    console.log("falsoss");
    return false;
  }
}
