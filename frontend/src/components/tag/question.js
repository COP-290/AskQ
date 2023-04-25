import { useEffect,useState } from "react";
import "highlight.js/styles/github.css";
import hljs from "highlight.js";
import { useNavigate, useParams } from "react-router-dom";
import { PaginationControl } from 'react-bootstrap-pagination-control';
import Q from "./q";

export default function Question() {

  const [data,setdata] = useState(null);
  const [page, setPage] = useState(1)
  const [sortby,setSortby] = useState('/score');
  const [number, setNumber] = useState(0)
  const { id } = useParams(); 
  console.log(id);

  let navigate = useNavigate();
  const to = async (id) => {
    let path = `/${id}`;
    navigate(path);
  //   await scroller.scrollTo("head", {
  //     duration: 1500,
  //     offset: 0,
  //   });
  };

  useEffect(() => {
    hljs.highlightAll();
  });

  function newq(){
    fetch('/user').then((res) =>
        res.json().then((dat) => {
          console.log(dat)
          if (dat===false){to('login')}
          else {to('new_question')}
        })
    );
  }

  useEffect(() => {
    console.log(sortby)
    fetch(id?`/${encodeURIComponent(id.trim())}/${page}${sortby}/question`:`${sortby}/question/${page}`).then((res) =>
        res.json().then((data) => {
            console.log(data);
            setdata(data)
        })
    );
  }, 
  [page,sortby]
  );


useEffect(() => {
    fetch(id?`/${encodeURIComponent(id.trim())}/question/number`:`/question/number`).then((res) =>
        res.json().then((data) => {
            console.log(data);
            setNumber(parseInt(data))
        })
    );
}, []); 

    return (
        <>
        <body style={{"font-weight":"600 !important"}}>

<div class="row">

<div class="page_title p-1 d-flex justify-content-center">
    {id?`${id}`:"Questions"}
</div>


<div class ="col-12 px-4 d-flex justify-content-end">
  <button type="button" class="btn btn-success ask_btn"  onClick={()=>newq()}>
    <a class=" ask_btn">Ask question</a>
  </button>
</div>

<div class="row col-12 px-3 d-flex justify-content-start">
  <div class="dropdown col-12 px-4 ">
    <button  class="sorting_box btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
      Sorting
    </button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" style={{"cursor":"pointer"}} onClick={()=>setSortby('/time')}>Newest</a></li>
      {/* <li><a class="dropdown-item" href="#">Active</a></li> */}
      <li><a class="dropdown-item" style={{"cursor":"pointer"}} onClick={()=>setSortby('/score')}>Score</a></li>
    </ul>
  </div>
</div>

{/* <div class="row d-flex justify-content-start">
  <div class="col-12 d-flex justify-content-start" style={{"font-size": "larger"}}>
    <div class="px-3 py-2">
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <label class="filter_box input-group-text" for="inputGroupSelect01">Filters</label>
        </div>
        <select class="custom-select" style={{"border-radius": "2.75px","color": "3A4D3A"}} id="inputGroupSelect01">
          <option class="filter_option" selected>choose filter.. </option>
          <option class="filter_option" value="1">fitler-1</option>
          <option class="filter_option" value="2">fitler-2</option>
          <option class="filter_option" value="3">fitler-3</option>
        </select>
      </div> 
    </div> 
  </div>  
</div> */}

{data?  Object.entries(data).map(([key,value])=>
<><Q value={value}/></>
)


:<></>}

</div>

    <div class="pagination d-flex justify-content-center" >
        <PaginationControl
            page={page}
            between={3}
            total={number?number:0}
            limit={3}
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