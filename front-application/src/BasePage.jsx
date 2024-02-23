import React, { Fragment } from "react";
import { Route, Routes } from "react-router-dom";
import Home from "./Components/WebSite/Home/Home";
import About from "./Components/WebSite/InnerPages/About/About";
import Team from "./Components/WebSite/InnerPages/Team/Team";
import Event from "./Components/WebSite/InnerPages/Event/Event";
import Organizer from "./Components/WebSite/InnerPages/Organizer/Organizer";
import Contact from "./Components/WebSite/InnerPages/Contact/Contact";
import DashboardBase from "./Components/DashboardPanel/DashboardBase/DashboardBase";
const BasePage = () => {
  return (
    <Fragment>
      <Routes>
        <Route path="*" element={<Home />} />
        <Route path="about" element={<About />} />
        <Route path="about" element={<About />} />
        <Route path="team" element={<Team />} />
        <Route path="event" element={<Event />} />
        <Route path="organizer" element={<Organizer />} />
        <Route path="contact" element={<Contact />} />
        <Route path="/dashboard/*" element={<DashboardBase />} />
      </Routes>
    </Fragment>
  );
};

export default BasePage;
