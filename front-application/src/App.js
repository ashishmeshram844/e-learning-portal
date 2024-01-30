import { Fragment } from "react";
import styles from "./static/css/index-page/index.module.css"
import Navbar  from "./Components/Base/Navbar";
import Slider from "./Components/Slider/Slider"
import Achievements from "./Components/Achievements/Achievements"
import CoursesWorkflow from "./Components/CoursesWorkflow/CoursesWorkflow"
import Instructors from "./Components/Instructors/Instructors"
import Services from "./Components/Services/Services"
import LiveTutoring from "./Components/LiveTutoring/LiveTutoring"
import Footer  from "./Components/Base/Footer";
function App() {
  return (
    <Fragment>
      <div className={styles.App_Main}>
        <Navbar />
        <Slider />
        <Achievements />
        <CoursesWorkflow />
        <Instructors />
        <Services />
        <LiveTutoring />
        <Footer />
      </div>
    </Fragment>
  );
}

export default App;
