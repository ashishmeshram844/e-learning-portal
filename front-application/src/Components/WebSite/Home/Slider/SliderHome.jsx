import React, { Fragment, useEffect, useState } from "react";
import styles from "./Slider.module.css";
import jsonData from "./SliderMet.json";

const SliderHome = () => {
  const [active, setActive] = useState(0);
  const [autoplay, setAutoplay] = useState(true);
  const max = jsonData.length;
  const intervalBetweenSlides = () =>
    autoplay && setActive(active === max - 1 ? 0 : active + 1);
    useEffect(() => {
      const interval = setInterval(() => intervalBetweenSlides(), 3000);
      return () => clearInterval(interval);
  });
  const toggleAutoPlay = () => setAutoplay(!autoplay);

  const nextOne = () => {
    if(max === max){
      active < max - 1 && setActive(active + 1)
    }else{
      active > 0 && setActive(max)
    }
  };
  const prevOne = () => active > 0 && setActive(active - 1);

  const isActive = (value) => active === value && "active";
  const setSliderStyles = () => {
    let transition = active * -100;
    return {
      width: jsonData.length * 100 + "vw",
      transform: "translateX(" + transition + "vw)",
    };
  };


  return (
    <Fragment>
      <div className={styles.SliderMain}>
        <div className="grid grid-cols-12">
          <div className="col-span-12">
            <div className={styles.SliderWrap} style={setSliderStyles()}>
              {jsonData.map((item, index) => (
                <div className={styles.SliderItem} key={index} style={{ backgroundImage: item.slideImage }} ></div>
              ))}
            </div>
            <div className={styles.SliderPlay}>
              <SliderPlay 
                prevOne={prevOne}
                nextOne={nextOne}
                toggleAutoPlay={toggleAutoPlay}
                autoplay={autoplay}
                setActive={setActive}
                isActive={isActive}
              />
            </div>
          </div>
        </div>
      </div>
    </Fragment>
  );
};


const SliderPlay = ({toggleAutoPlay, prevOne, autoplay, isActive, nextOne, setActive}) =>{
  return(
    <Fragment>
      <div className={styles.SliderArrowPrev}>
        <button type="button" className="inline-flex gap-2" onClick={() => prevOne()}>
          <i className="icon-line_start_arrow_notch"></i>
        </button>
      </div>
      <div className={styles.SliderAutoPlay}>
        <button className="inline-flex" type="button" onClick={toggleAutoPlay}>
          {autoplay ?  <i className="icon-play_circle text-green-500"></i> :   <i className="icon-pause_circle text-red-500"></i>}
        </button>
      </div>
      <div className={styles.SliderDot}>
        {jsonData.map((silde,index) => (
          <button  onClick={() => setActive(index)} className={isActive(index) ? styles.SliderActiveDot : styles.SliderNotActiveDot} key={index}></button>
        ))}
      </div>
      <div className={styles.SliderArrowNext}>
        <button type="button" className="inline-flex gap-2" onClick={() => nextOne()}>
          <i className="icon-line_end_arrow_notch"></i>
        </button>
      </div>
    </Fragment>
  )
}

export default SliderHome;
