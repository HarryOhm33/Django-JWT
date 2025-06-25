// src/pages/VerifyOtp.jsx
import { useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";
import { useAuth } from "../contexts/AuthContext";

const VerifyOtp = () => {
  const [otp, setOtp] = useState("");
  const { verifyOtp } = useAuth();

  const handleVerify = async (e) => {
    e.preventDefault();
    await verifyOtp(otp);
  };

  return (
    <form onSubmit={handleVerify}>
      <input
        placeholder="Enter OTP"
        value={otp}
        onChange={(e) => setOtp(e.target.value)}
      />
      <button type="submit">Verify OTP</button>
    </form>
  );
};

export default VerifyOtp;
