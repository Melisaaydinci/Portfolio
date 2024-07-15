import { useState, useEffect } from "react";

const Projects = () => {
  const [Projects, setProjectsData] = useState([]);

  const fetchData = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/get_projects");
    const data = await response.json();
    console.log(data);
    setProjectsData(data);
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <section className="bg-bg_light_primary" id="projects">
      <div className="md:container px-5 pt-14 min-h-[50vh] flex flex-col">
        <h2 className="titles mb-0" data-aos="fade-down">
          Projeler
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 mt-5 mb-0 pb-0">
          {Projects.map((content, i) => (
            <div
              key={i}
              className="bg-white rounded-3xl p-5 border-b-8 border-[#FAF9FD] flex flex-col justify-start items-center"
              style={{ minHeight: '250px' }} // Kartların boyutlarını eşitlemek için
            >
              <h5 className="font-bold font-Poppins m-0 p-0">
                {content.name}
              </h5>
              
              <div className="flex flex-col text-center w-full mb-0 pb-0">
                <h5 className="font-Poppins m-0 p-0">
                  {content.definition}
                </h5>
              </div>
            </div>
          ))}
        </div>
        <br />
      </div>
    </section>
  );
};

export default Projects;
