export default function Main(){
    return(
        <>
        <body class="main_fonts px-5 ">
                <div class="d-flex flex-column main_row mt-3">
                    <div class="row mx-3 col-12 d-flex justify-content-center">
                        <div class="main_lines p-4 ">
                        <inst1><inst>Problem ?</inst> Not able to find the solution ?</inst1>
                        </div>
                    </div>
                    <div class="row  mx-3 col-12 mt-1 d-flex justify-content-center">
                        <div class="main_lines p-4 ">
                        <inst1>Are you spending too much <inst>time</inst> on other websites trying to find <inst>solution ?</inst></inst1>
                        </div>
                    </div>
                    <div class="row  mx-3 col-12 mt-1 d-flex justify-content-center">
                        <div class="main_lines p-4 mb-3">
                            <inst1>To cope with these type of problems here we comewith </inst1> 
                            <center>
                                <div class="navbar-brand ps-2">askQ.com</div>
                            </center>
                        </div> 
                    </div>    
                </div>
                <div id="carouselExampleIndicators" class="carousel slide m-3" data-bs-ride="true">
                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
                </div>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="https://www.technocrazed.com/wp-content/uploads/2015/12/beautiful-wallpaper-download-14.jpg" class="d-block w-100" alt="..."/>
                        <div class="carousel-caption d-none d-md-block">
                            <h5>First slide label</h5>
                            <p>Some representative placeholder content for the first slide.</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://i0.wp.com/digital-photography-school.com/wp-content/uploads/2019/02/Landscapes-04-jeremy-flint.jpg?fit=1500%2C1000&ssl=1" class="d-block w-100" alt="..."/>
                        <div class="carousel-caption d-none d-md-block">
                            <h5>Second slide label</h5>
                            <p>Some representative placeholder content for the first slide.</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://images.unsplash.com/photo-1509043759401-136742328bb3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80" class="d-block w-100" alt="..."/>
                        <div class="carousel-caption d-none d-md-block">
                            <h5>Third slide label</h5>
                            <p>Some representative placeholder content for the first slide.</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://www.eventstodayz.com/wp-content/uploads/2018/08/beautiful-hd-wallpaper.jpg" class="d-block w-100" alt="..."/>
                        <div class="carousel-caption d-none d-md-block">
                            <h5>Forth slide label</h5>
                            <p>Some representative placeholder content for the first slide.</p>
                        </div>
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </body>
        </>
    );
}