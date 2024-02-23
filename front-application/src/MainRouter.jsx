import React, { Fragment } from "react";
import { Routes, Route } from "react-router-dom";
import Login from "./Components/Auth/Login";
import Register from "./Components/Auth/Register";
import ForgotPassword from "./Components/Auth/ForgotPassword";
import BasePage from "./BasePage";
const MainRouter = () => {
  return (
    <Fragment>
      <Routes>
        <Route path="*" element={<BasePage />} />
        {/* <Route path={"/login"} element={<Login />} /> */}
        {/* <Route path={"/register"} element={<Register />} /> */}
        {/* <Route path={"/forgot-password"} element={<ForgotPassword />} /> */}
      </Routes>
    </Fragment>
  );
};

export default MainRouter;
