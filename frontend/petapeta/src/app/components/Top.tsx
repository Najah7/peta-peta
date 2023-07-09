"use client";
import { useState } from "react";
import Card from "./Card";
import PostCard from "./PostCard";

function Top() {
  const [cardPosition, setCardPosition] = useState({ top: 0, left: 0 });

  const handleClick = (e: React.MouseEvent<HTMLDivElement>) => {
    console.log("clicked");
    setCardPosition({ top: e.clientY, left: e.clientX });
    console.log({ top: e.clientY, left: e.clientX });
  };
  return (
    <>
      <div
        style={{
          position: "absolute",
          width: "100vw",
          height: "100%",
          opacity: 0,
        }}
        onClick={handleClick}
      ></div>
      <Card top={cardPosition.top} left={cardPosition.left} />
      <PostCard />
      <PostCard />
      <PostCard />
      <PostCard />
    </>
  );
}

export default Top;
