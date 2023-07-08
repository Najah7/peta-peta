"use client";
import React, { useState } from "react";
import Card from "../components/Card";

const About: React.FC = () => {
  const [cardPosition, setCardPosition] = useState({ top: 0, left: 0 });

  const handleClick = (e: React.MouseEvent<HTMLDivElement>) => {
    console.log("clicked");
    setCardPosition({ top: e.clientY, left: e.clientX });
    console.log({ top: e.clientY, left: e.clientX });
  };

  return (
    <div
      style={{
        backgroundColor: "red",
        width: "100vw",
        height: "100vh",
        position: "relative",
      }}
      onClick={handleClick}
    >
      <Card top={cardPosition.top} left={cardPosition.left} />
    </div>
  );
};

export default About;
