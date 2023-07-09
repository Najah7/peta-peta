type PostItProps = {
  comment: string;
};

const PostIt: React.FC<PostItProps> = ({ comment }) => {
  return (
    <div
      className="card"
      style={{
        position: "relative",
        top: "-30px",
        width: "20vw",
        margin: "0 5px",
        backgroundColor: "#eee",
        boxShadow: "0 0 5px #aaa",
        padding: "20px",
        paddingBottom: "60px",
      }}
    >
      <div>{comment}</div>
    </div>
  );
};

export default PostIt;
