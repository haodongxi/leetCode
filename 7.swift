
class Solution {
    func reverse(_ x: Int) -> Int {
        var numStr:String = String(format:"%0.f",fabs(Double(x)))
        numStr = String(numStr.reversed())
        var result:Double! = Double(numStr)
        if x<0{
            result = 0-result
        }
        if (result > (pow(2, 31)-1) || result < -pow(2,31)){
            return 0
        }
        return Int(result)
    }
}

