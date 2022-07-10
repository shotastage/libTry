//
//  DemoFinder.swift
//  
//
//  Created by Shota Shimazu on 2022/07/10.
//

import Foundation


open class DemoFinder {
    
    let directoryIdentifier = [
        "Example",
        "Sample"
    ]

    func find() {
        for identifer in directoryIdentifier {
            print(identifer)
        }
    }
}
