function completado() {
    Swal.fire(
        '¡Éxito!',
        'Se ha s el reporte correctamente',
        'success'
    )
    timer = 0;
    while (timer !== 20000){
        console.log(timer);
        timer++;
    }
}
