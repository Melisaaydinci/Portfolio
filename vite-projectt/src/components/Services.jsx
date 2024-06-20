import { content } from "../Content";
import {  useState ,useEffect} from "react";
const Services = () => {
  
  const [Services, setServicesData] = useState([]);
  const fetchData = async () => {
    const response = await fetch(" http://127.0.0.1:8000/api/get_services");
    const data = await response.json();
    console.log(data)
    setServicesData(data);
    
    }

    useEffect(() => {
    fetchData();
    }, []);
    
  return (
    <section id="services">
      <div className="md:container px-5 py-14">
        <h2 className="title" data-aos="fade-down">
          Çalışma Alanlarım
        </h2>
        <br />
        <div className="flex gap-5 justify-between flex-wrap group">
          {Services.map((content, i) => (
            <div
              key={i}
              data-aos="fade-up"
              data-aos-delay={i * 600}
              className="min-w-[14rem] duration-300 cursor-pointer border-2 border-slate-200 rounded-xl text-center bg-bg_light_primary p-6 flex-1 group-hover:blur-sm 
              hover:!blur-none"
            >
              
              <h6 className="my-3">{content.name}</h6>
              <p className="leading-7">{content.definition}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Services;
