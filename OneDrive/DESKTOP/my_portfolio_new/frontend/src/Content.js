// import images
import Hero_person from "./assets/images/Hero/person.png";
import Ben from "./assets/images/Hero/ben.png";


import figma from "./assets/images/Skills/figma.png";
import css from "./assets/images/Skills/css.png";
import django from "./assets/images/Skills/django.png";
import html from "./assets/images/Skills/html.png";
import js from "./assets/images/Skills/js.png";
import python from "./assets/images/Skills/python.png";
import c from "./assets/images/Skills/c.png";
import unity from "./assets/images/Skills/unity.png";
import postgresql from "./assets/images/Skills/postgresql.png";





// import icons from react-icons
import { GrMail } from "react-icons/gr";
import { MdArrowForward, MdCall } from "react-icons/md";
import { TbSmartHome } from "react-icons/tb";
import { BiUser } from "react-icons/bi";
import { RiServiceLine, RiProjectorLine } from "react-icons/ri";
import { MdOutlinePermContactCalendar } from "react-icons/md";
import { FaGithub } from 'react-icons/fa';

export const content = {
  nav: [
    {
      link: "#home",
      icon: TbSmartHome,
    },
    {
      link: "#skills",
      icon: BiUser,
    },
    {
      link: "#services",
      icon: RiServiceLine,
    },
    {
      link: "#projects",
      icon: RiProjectorLine,
    },
    {
      link: "#contact",
      icon: MdOutlinePermContactCalendar,
    },
  ],
  hero: {
    title: "Full Stack Developer",
    firstName: "Melisa",
    LastName: "Aydıncı",
    btnText: "Hire Me",
    image: Ben,
    hero_content: [
      {
        count: "2+",
        text: "Yıllık Tecrübe",
      },
      {
        count: "5+",
        text: "Çalıştığım Projeler",
      },
    ],
  },
  skills: {
    title: "Yetenekler",
    skills_content: [
      {
        name: "C",
        logo: c,
      },
      {
        name: "Python",
        logo: python,
      },
      {
        name: "Django",
        logo: django,
      },
      {
        name: "Html",
        logo: html,
      },
      {
        name: "Css",
        logo: css,
      },
      {
        name: "Javascript",
        logo: js,
      },
      {
        name: "Postgresql",
        logo: postgresql,
      },
      {
        name: "Figma",
        logo: figma,
      },
      {
        name: "Unity",
        logo: unity,
      },
    ],
    icon: MdArrowForward,
  },

  Contact: {
    title: "İletişim",
    social_media: [
      {
        text: "melisaaydinci62@gmail.com",
        icon: GrMail,
        link: "mailto:melisaaydinci62@gmail.com",
      },
      {
        text: "+534 933 3960",
        icon: MdCall,
        link: "https://wa.me/1234567890",
      },
      {
        text: "Melisa Aydıncı",
        icon: FaGithub, // Github iconu burada
        link: "https://github.com/Melisaaydinci",
        
      },
    ],
  },
  Footer: {
    text: "All © Copy Right Reserved 2024",
  },
};
