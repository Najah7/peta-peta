type CardProps = {
  top: number;
  left: number;
};

const Card: React.FC<CardProps> = ({ top, left }) => {
  const saveComment = () => {
    console.log("save comment");
  };

  return (
    <div
      className="card"
      style={{
        position: "absolute",
        top: top,
        left: left,
        width: "20vw",
        backgroundColor: "#eee",
        boxShadow: "0 0 5px #aaa",
        padding: "20px",
        paddingBottom: "60px",
      }}
    >
      <textarea name="comment" placeholder="コメント"></textarea>
      <div>
        <button onClick={saveComment}>投稿!!</button>
      </div>
    </div>
  );
};

export default Card;
