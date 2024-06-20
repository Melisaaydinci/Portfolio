// import content
import { useEffect ,useState} from "react";
import { content } from "../Content";
const Hero = () => {
  const { hero } = content;
  const [Hero, setHeroData] = useState([]);
  const fetchData = async () => {
    const response = await fetch(" http://127.0.0.1:8000/api/get_personel");
    const data = await response.json();
    console.log(data)
    setHeroData(data);
    
    }

    useEffect(() => {
    fetchData();
    }, []);

    const handleDownload = (url) => {
      // Dosya indirme işlemini başlat
      const link = document.createElement('a');
      link.href = url;
      link.target = '_blank';
      // link.download özelliğini belirtmiyoruz, tarayıcı dosya ismini URL'den alacak
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    };
    
  return (
    <section id="home" className="overflow-hidden">
      <div className="min-h-screen relative flex md:flex-row flex-col-reverse md:items-end justify-center items-center">
        <div
          data-aos="slide-left"
          data-aos-delay="1200"
          className="absolute h-full md:w-4/12 w-8/12 top-0 right-0 bg-primaryLinear bottom-0 -z-10"
        >
          <h1 className="rotate-90 absolute top-[30%] right-[-15%] text-[#EAF2FA]">
            {Hero.first_name}{" "}
            <span className="text-dark_primary">{Hero.last_name}</span>
          </h1>
        </div>

        {/* first col */}
        <div className="pb-16 px-6 pt-5" data-aos="fade-down">
          <h2>{Hero.profession}</h2>
          <br />
          <div className="flex flex-col gap-10 mt-10">
              <div
                data-aos="fade-down"
                data-aos-delay={0 * 300}
                className={`flex items-center w-80 gap-5
             `}
              >
                <p>{Hero.definition}</p>
              </div>
          </div>
          <br /><br /><br />
          <div className="flex justify-end">
            <button className="btn" onClick={() => handleDownload(Hero.cv)}>
              Özgeçmişi İncele
            </button>
          </div>        
        </div>

        {/* sec col */}
        <div className="md:h-[37rem] h-96">
          <img
            src={Hero.photo}
            data-aos="slide-up"
            alt="..."
            className="h-full object-cover"
          />
        </div>
      </div>
    </section>
  );
};

export default Hero;
