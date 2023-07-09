"use client";
import { useState } from "react";
import PostCard from "./PostCard";

function Top() {
  const [cardPosition, setCardPosition] = useState({ top: 0, left: 0 });
  const [comment, setComment] = useState("");

  const [firstPost, setFirstPost] = useState([
    { comment: "aaa", top: -400, left: 500 },
    { comment: "bbb", top: -500, left: 700 },
    { comment: "ccc", top: -1000, left: 200 },
    { comment: "ddd", top: -10, left: 600 },
  ]);

  const handleClick = (e: React.MouseEvent<HTMLDivElement>) => {
    console.log("clicked");
    setCardPosition({ top: e.clientY, left: e.clientX });
    console.log({ top: e.clientY, left: e.clientX });
    //firstPostの配列に新しオブジェクトを追加して新しい配列を作る
    const firstPostCopy = [
      ...firstPost,
      { comment: "test", top: e.clientY, left: e.clientX },
    ];
    // setFirstPost(firstPostCopy);
  };

  const saveComment = () => {
    console.log("save comment");
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
      <div
        className="card"
        style={{
          position: "absolute",
          top: cardPosition.top,
          left: cardPosition.left,
          width: "20vw",
          backgroundColor: "#eee",
          boxShadow: "0 0 5px #aaa",
          padding: "20px",
          paddingBottom: "60px",
        }}
      >
        <textarea onChange={} name="comment" placeholder="コメント"></textarea>
        <div>
          <button onSubmit={saveComment}>投稿!!</button>
        </div>
      </div>
      <PostCard
        username="山田隼人"
        comment="たのしー！！！"
        imgPath="/postimage.jpg"
        note={6}
        post={firstPost}
      />
      <PostCard
        username="鎌田美佑"
        comment="たのしー！！！"
        imgPath="/postimage1.jpg"
        note={10}
        post={[
          { comment: "eee", top: -200, left: 800 },
          { comment: "fff", top: -100, left: 1000 },
          { comment: "ggg", top: -1200, left: 500 },
          { comment: "hhh", top: -70, left: 600 },
        ]}
      />
      <PostCard
        username="松尾ナジャ"
        comment="たのしー！！！"
        imgPath="/postimage2.jpg"
        note={5}
        post={[
          { comment: "eee", top: -200, left: 800 },
          { comment: "fff", top: -100, left: 1000 },
          { comment: "ggg", top: -1200, left: 500 },
          { comment: "hhh", top: -70, left: 600 },
        ]}
      />
      <PostCard
        username="コエチ ユウマ"
        comment="たのしー！！！"
        imgPath="/postimage3.png"
        note={1}
        post={[
          { comment: "eee", top: -200, left: 800 },
          { comment: "fff", top: -100, left: 1000 },
          { comment: "ggg", top: -1200, left: 500 },
          { comment: "hhh", top: -70, left: 600 },
        ]}
      />
    </>
  );
}

export default Top;
