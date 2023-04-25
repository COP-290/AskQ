import {useEffect,useState} from 'react'
import {useNavigate} from 'react-router-dom'
import { PaginationControl } from 'react-bootstrap-pagination-control';

export default function User() {
    const [data,setdata] = useState('/score');
    const [page, setPage] = useState(1)
    const [number, setNumber] = useState(3100)


    useEffect(() => {
        fetch(`/users/${page}`).then((res) =>
            res.json().then((data) => {
                // console.log(data);
                setdata(data)
            })
        );
    }, [page]);

    let navigate = useNavigate();
    const to = async (id) => {
      let path = `/${id}`;
      navigate(path);    
    }
    return(

        <>
        <body>
            <div class="page_title p-1 d-flex justify-content-center mt-3">
            Users 
            </div>
            {/* <div class="dropdown col-12 px-4 d-flex justify-content-center">
                <button  class="sorting_box btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Sorting
                </button>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" style={{"cursor":"pointer"}} onClick={()=>setSortby('/time')}>Newest</a></li>
                    <li><a class="dropdown-item" style={{"cursor":"pointer"}} onClick={()=>setSortby('/score')}>Score</a></li>
                </ul>
            </div> */}
            <div class="d-flex justify-content-center mt-3">
                <div class="col-7 px-3 py-2">
                    <form action="/action_page.php" style={{ "border-radius":"7px"}}>
                        <input class="form-control" list="tags" name="tag" id="tag" placeholder="Search the filter.."></input>
                        <datalist id="tags">
                        <option value="Python"/>
                        <option value="JavaScript"/>
                        <option value="MySQL"/>
                        <option value=""/>
                        <option value="Safari"/>
                        </datalist>    
                    </form>
                </div>
            </div>
            <div class="row d-flex flex row m-3">
            {data?
            Object.entries(data).map(([key,value])=>
            <div class="tag_col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-6 p-3" onClick={()=>to(`user/${value[0]}`)}>
            <div class="user_box p-3">
                <div class="user_pic d-flex justify-content-center" style={{"font-family": "'Roboto Mono', monospace"}}>
                    <div>
                        {value[9]?<img src={value[9]} width="60" height="60" style={{"border-radius":"50%"}}></img>:
                        <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16" >
                            <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                            <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                        </svg>}
                    </div> 
                </div>
                <div class="username d-flex justify-content-center" style={{" color": "rgb(88, 88, 88)"}} > 
                    {value[1]}
                </div>
                <div class="user_reputation d-flex justify-content-center ">
                    {value[6]}
                </div>
            </div>
        </div>     
        ):<></>}

            </div>  
            <div class="pagination mt-2 col-12 d-flex justify-content-center" >
        <PaginationControl
            page={page}
            between={3}
            total={number?number:0}
            limit={30}
            changePage={(page) => {
            setPage(page); 
            console.log(page)
            }}
            ellipsis={1}
        />
    </div>     
        </body>
        </>
    );
}